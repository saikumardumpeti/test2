from frappe import _
def get_context(context):
    context.aa = _('Custom Page')
    context.text = "Hello this is a frappe custom page"
    return context



