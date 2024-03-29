from frontend.models import *
from matrixpro.models import *
import itertools




setting_mod =  SettingModel.objects.all()

def getDownloads():
    container  = []
    get_downs = Downloads.objects.all()
    
    for x in get_downs:
        get_downconent = DownloadContent.objects.all().filter(download_id=x.id)
        if get_downconent.exists():
            cnt = []
            for cont in get_downconent:
                cnt.append({
                    'title':cont.title,
                    'link':cont.link
                })
            container.append({'title':x.name, 'logo':x.logo, "files": cnt })
    return container


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
        propaty = MatrixProperty.objects.all().filter(property_type_id=m_type.id, active='yes').order_by('index')
        
        if propaty.count() > 0:
            container.append({"shortname":f"{m_type.name.replace('','_')}", "name":f"{m_type.name}", "data":propaty})

    return container

def getBranches():
    
    branchesModel  = BranchModel.objects.all()
    branches = [
        {
        'id': branch.id, 
        'name': branch.name, 
        'image': branch.image.url, 
        'address': branch.address, 
        'tel': branch.tel,
        'email': branch.email,
        } for branch in BranchModel.objects.all()
    ]
    return branches

def getAddress():
    container = [{
            "icon":address.icon, 
            "title":address.title, 
            "link":address.link, 
            "position":address.position
        } for address in  Address.objects.all().order_by('index')
    ]
    return container


def getAbout(request):
    about = AboutModel.objects.all()
    if about.exists():
        return {"about":about[0].about}
    return {"about":""}

def getMenus():
    estate = MenusModel.objects.filter(link="/estates").order_by("index")
    if estate.exists():
        for prop in MatrixProperty.objects.all():
            try:
                menuChildCheck = MenuChildModel.objects.filter(title=prop.property_title)
                if not menuChildCheck.exists():
                    menuChild = MenuChildModel.objects.create(
                        menu_id=estate.first().id,
                        title=prop.property_title,
                        link = f'/property_detail/{prop.id}/'
                    )
                    # print(menuChild)
            except Exception as e:
                # print(e)
                return f"{e}"
            
    container  = []
    menus = MenusModel.objects.all().order_by("index")
    
    for menu in menus:
        menu_children = MenuChildModel.objects.all().filter(menu_id=menu.id)
        menu_dict = {'title':menu.title, 'link':menu.link, 'has_children':menu.has_children}
        if menu_children.exists():
            children = []
            for child in menu_children:
                children.append({
                    'title':child.title,
                    'link':child.link
                })
            menu_dict['children'] = children
        container.append(menu_dict)
    return container


# 
def getTelevision():
    televisions = [{"title":tv.title, "youtube":tv.youtube, "description":tv.description} for tv in Television.objects.all()]
    return televisions

def getPageTitle(request):
    if request.path == "/":
        title = 'Home - '
    else:
        # title = str(request.path).replace('/', '').title()
        title = str(request.path).split('/')[1].title() + ' - '
        path = str(request.path).split('/')[1]
        if path == 'property_detail':
            title = "Property Detail - "
        else:
            title = path.title() + ' - '
    return title


def getFrontEndAgents():
    agents = FrontEndAgent.objects.all().order_by('?')
    return agents


def httpPattern(url):
    import re
    try:
        pattern = re.compile(r'(http[s]?://[^:/]+:\d+)')
        match = pattern.search(url)
        if match:
            # Retrieve the captured part of the URL and add a trailing '/'
            cleaned_url = match.group(1)
            return cleaned_url
        else:
            return ""
    except:
        pass


def frontendContent(request):
    url_path = httpPattern(request.META.get("HTTP_REFERER", "https://vaticanprojects.com"))
    data = list(MatrixProperty.objects.all())
    
    context = {}
    context['wsgi_protocol'] = url_path
    context['youtube'] = YoutubeModel.objects.all().filter(is_active=True)
    context['sliders'] = Slider.objects.all().filter(is_showed=True).order_by("index")
    context['properties'] = getProperties()
    # context['properties'] = groupingItem(item=data)
    context['testimonials'] = groupingItem(item=list(MatriproTestimonal.objects.all().filter(control=True).order_by('created')))
    context['services'] = groupingItem(list(MatriproxServices.objects.all().order_by('index')))
    context['latest_news'] = groupingItem(
        item=list(MatriproxBlog.objects.all().filter(status=True).order_by("created")),
         group_size=2
        )
    context['downloads'] = getDownloads()
    
    
    context['settings'] = {
        'branches': getBranches(),
        'address':getAddress(),
        'about':getAbout(request)["about"],
        'short_footer_desc':setting_mod.first().aboutus,
        'site_logo':setting_mod.first().site_logo,
        # # 'site_logo':'logo.png',
        'site_title':setting_mod.first().site_title,
        # 'site_subtitle':getAbout(request)["site_subtitle"],
        'menus':getMenus(),
        "setings_package":setting_mod.first()
        # 'contacts':BranchModel.objects.all().filter(is_active=True),
    }
    context['television'] = getTelevision()
    context['page_title'] = getPageTitle(request)
    context['front_agent'] = getFrontEndAgents()
    return context