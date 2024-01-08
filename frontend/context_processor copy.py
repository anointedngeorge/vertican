from frontend.models import *
from matrixpro.models import *
import itertools

def getDownloads():
    container  = {}
    get_downs = Downloads.objects.all()
    
    for x in get_downs:
        get_downconent = DownloadContent.objects.all().filter(download_id=x.id)
        cnt = []
        for cont in get_downconent:
            cnt.append({
                'title':cont.title,
                'link':cont.link
            })
        container.update({'title':x.download.name, 'logo':x.download.logo, "files": cnt })
    
    
    


def groupingItem(item, group_size=4):
    container = []
    for i in range(0, len(item), group_size):
        group = item[i:i+group_size]
        container.append(group)
    return container


def getProperties():
    container = []
    m_types = MatrixPropertyType.objects.all().order_by("index")
    
    for m_type in m_types:
        propaty = MatrixProperty.objects.all().filter(property_type_id=m_type.id)
        
        if propaty.count() > 0:
            container.append({"shortname":f"{m_type.name.replace('','_')}", "name":f"{m_type.name}", "data":propaty})

    return container


def frontendContent(request):
    data = list(MatrixProperty.objects.all())
    context = {}
    context['youtube'] = YoutubeModel.objects.all().filter(is_active=True)
    context['sliders'] = Slider.objects.all().filter(is_showed=True)
    context['properties'] = getProperties()
    # context['properties'] = groupingItem(item=data)
    context['testimonials'] = groupingItem(item=list(MatriproTestimonal.objects.all().filter(control=True).order_by('created')))
    context['services'] = groupingItem(list(MatriproxServices.objects.all().order_by('index')))
    context['latest_news'] = groupingItem(
        item=list(MatriproxBlog.objects.all().filter(status=True).order_by("created")),
         group_size=2
        )

    context['settings'] = {
        'branches': [
            {'id':'lagos', 'name':'Lagos', 'image':'https://ceeplat.com/wp-content/uploads/2021/07/IMG_0260-e1626952105277.jpg', 
             'address':"Suite 22A Primal Tek Plaza, 133, Okota Road, Okota, Lagos", 'tel':'+234-809-164-7093, 090-8482-3980','email':'info@ceeplat.com'},

            {'id':'asaba', 'name':'Asaba', 'image':'https://ceeplat.com/wp-content/uploads/2021/07/Lagos231-e1626950836825.jpeg', 
             
             'address':'Suite 26 De-Park Plaza, 135, Ibusa Road, Opposite Ministry Of Lands & Survey, Asaba', 'tel':'+234-812-122-9438, 080-9164-7093','email':'asaba@ceeplat.com'},
            
            {'id':'head_office', 'name':'Head Office', 'image':'https://ceeplat.com/wp-content/uploads/2021/07/5N2A3361-e1626952768198.jpg', 
             'address':'No 23 Liberty Estate Phase 2 Independence Layout, Enugu', 
             'tel':'+234-708-360-0327, 080-9164-7093','email':'enugu@ceeplat.com',
            },
        ],
        'address':[
            {'icon':'fa fa-phone', 'title':'08091647093', 'link':'','position':'left'},
            {'icon':'fa fa-map-marker', 'title':'65 North Park Bwe, USA', 'link':'','position':'left'},
            {'icon':'fa fa-envelope-o', 'title':'enugu@ceeplat.com', 'link':'','position':'left'},

            {'icon':'fa fa-user', 'title':'Email Login', 'link':'','position':'right'},
            # {'icon':'fa fa-sign-in', 'title':'Sign in', 'link':'','position':'right'},
        ],

        'about':'''
            Ceeplatprofile Ltd is a Real estate Development, Brokerage and Management 
            Company incorporated in Nigerian to provide global and best practices in real 
            estate investment services to private and portfolio investors in Nigeria and 
            around the world.
            Ceeplatprofile currently has established branch offices in Lagos, Asaba and Enugu.
        ''',

        'site_logo':'logo.png',
        'site_title':'Ceeplatprofile Ltd',
        'site_subtitle':'',

        # 'contacts':BranchModel.objects.all().filter(is_active=True),

        'menus': [
            {'title':'Home', 'link':'/', 'has_children':False, 'children': [
                {'title':'', 'link':''}
            ]},
            {'title':'About', 'link':'/about', 'has_children':False, 
                'children': [
                    {'title':'', 'link':''}
                ]
            },

            {'title':'Our Estates', 'link':'#', 'has_children':True, 
                'children': [{'title':prop.property_title, 'link':f'/property_detail/{prop.id}/'} for prop in MatrixProperty.objects.all() ]
            },

            {'title':'Vertican Garden Tv', 'link':'/television', 'has_children':False, 
                'children': []
            },

            {'title':'Downloads', 'link':'/downloads', 'has_children':False, 'children': [
                {'title':'', 'link':''}
            ]},

            {'title':'Contact', 'link':'/contact', 'has_children':False, 'children': [
                {'title':'', 'link':''}
            ]},
        ],
    }
    # close
    
    context['television'] = [
            {
                "title":'About Ceeplatprofile',
                "youtube":'<iframe width="430" height="242" src="https://www.youtube.com/embed/yTAPsiwB3rA" title="About Us @ CEEPLATPROFILE LTD" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>',
                'description':''
            },
             {
                "title":'FAQ',
                "youtube":'<iframe width="430" height="242" src="https://www.youtube.com/embed/ifPfr6-hrXU" title="FREQUENTLY ASKED QUESTION ON VATICAN GARDEN ESTATE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>',
                'description':''
            },
             {
                "title":'VGE Terms & Condition',
                "youtube":'<iframe width="430" height="242" src="https://www.youtube.com/embed/sPX_5xpHPLI" title="VATICAN GARDEN ESTATE TERMS AND CONDITION" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>',
                'description':''
            }
        ]
    
    context['downloads'] = [
        {'title':'Vatican Garden- Asaba', 'logo':'https://ceeplat.com/wp-content/uploads/2019/10/Beachfield-logo-2.png', 'files': [
            {'title':'Application Form', 'link':'http://vaticanasaba.ceeplat.com/wp-content/uploads/2019/09/Vatican-Garden-Estate-Asaba-Subscription-Form.pdf'},
            {'title':'Development Fees', 'link':'https://ceeplat.com/downloads/#'},
            {'title':'Transaction Fees', 'link':'http://vaticanasaba.ceeplat.com/wp-content/uploads/2019/09/CeeplatProfifle-Transaction-Process-1.pdf'},
            {'title':'FAQs', 'link':'http://vaticanasaba.ceeplat.com/wp-content/uploads/2019/09/ASABA-FREQUENTLY-ASKED-QUESTIONS.pdf'},
            {'title':'Layout', 'link':'http://vaticanasaba.ceeplat.com/wp-content/uploads/2019/09/Vatican-Garden-estate-Asaba-Layout2.png'},
        
        ]},

        {'title':'Vatican Garden- Asaba 2', 'logo':'https://ceeplat.com/wp-content/uploads/2019/10/Beachfield-logo-2.png', 'files': [
            {'title':'Application Form', 'link':'https://ceeplat.com/wp-content/uploads/2022/02/asaba-phase-2.pdf'},
            {'title':'Transaction process', 'link':'http://vaticanasaba.ceeplat.com/wp-content/uploads/2019/09/CeeplatProfifle-Transaction-Process-1.pdf'},
            {'title':'FAQs', 'link':'http://www.vaticanasaba2.com/wp-content/uploads/2020/06/PHASE-2-ASABA-FREQUENTLY-ASKED-QUESTION-.pdf'},
            {'title':'Layout', 'link':'https://www.vaticanasaba2.com/wp-content/uploads/2020/08/3D-LAYOUT-PHASE-2-ASABA.pdf'},
        ]},

        {'title':'Vatican Garden- Enugu', 'logo':'https://ceeplat.com/wp-content/uploads/2019/10/Beachfield-logo-2.png', 'files': [
            {'title':'Application Form', 'link':'https://ceeplat.com/wp-content/uploads/2022/02/ENUGU-PHASE-1-SUB-FORM.pdf'},
            {'title':'Development Fees', 'link':'https://ceeplat.com/downloads/#'},
            {'title':'Transaction Process', 'link':'http://vaticanenugu.ceeplat.com/wp-content/uploads/2019/09/CeeplatProfifle-Transaction-Process.pdf'},
            {'title':'FAQ', 'link':'http://vaticanenugu.ceeplat.com/wp-content/uploads/2019/09/VATICAN-GARDEN-ENUGU-FAQ-1.pdf'},
            {'title':'Layout', 'link':'https://ceeplat.com/wp-content/uploads/2019/12/Vatican-Garden-Enugu.pdf'},
        ]},


        {'title':'Vatican Garden- Enugu 2', 'logo':'https://ceeplat.com/wp-content/uploads/2019/10/Beachfield-logo-2.png', 'files': [
            {'title':'Application Form', 'link':'https://ceeplat.com/wp-content/uploads/2022/02/enugu-phase-2-1.pdf'},
            {'title':'Development Fees', 'link':'https://ceeplat.com/downloads/#'},
            {'title':'Online Application Form', 'link':'https://ceeplat.com/vatican-garden-estate-phase-2-subscription-form'},
            {'title':'FAQ', 'link':'https://vatican2enugu.ceeplat.com/wp-content/uploads/2021/07/FAQ-VATICAN-2-ENUGU-Copy-1.pdf'},
            {'title':'Layout', 'link':'https://ceeplat.com/wp-content/uploads/2022/04/FRAME1.jpg'},

        ]},
    ]
    return context