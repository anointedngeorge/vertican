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
        group = item[i:i+group_size]
        container.append(group)
    return container
