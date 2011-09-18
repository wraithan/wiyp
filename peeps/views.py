from lib.utils import render_to
from peeps.models import Peep

@render_to('peeps/all_peeps.html')
def all_peeps(request):
    peep_set = Peep.objects.all()
    return locals()
