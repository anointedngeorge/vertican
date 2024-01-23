from django import template

register = template.Library()




@register.simple_tag
def groupingItem(item, group_size=2):
    """
        Grouping items in group_sizes.
    """
    container = []
    for i in range(0, len(item), group_size):
        # group = {"features":item[i:i+group_size]}
        group = {"data":item[i:i+group_size]}
        container.append(group)
    return container


@register.simple_tag
def groupingItem1(item):
    """
        Grouping items in group_sizes.
    """
    container = []
    for i in range(0, len(item)):
        # group = {"features":item[i:i+group_size]}
        if i == 0:
            container.append({"data":item[i], "active":True})
        else:
            container.append({"data":item[i], "active":False})
    return container