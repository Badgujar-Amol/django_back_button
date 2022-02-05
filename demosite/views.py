from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Home page</h1> "
                        "<a href='page1'>Page 1</a> | "
                        " <a href='page2'>Page 2</a> | " 
                        " <a href='page3'>Page 3</a> | "
                        " <a href='page4'>Page 4</a> | "
                        " <a href='page5'>Page 5</a> "
                        )
def page1(request):
    return HttpResponse('Page 1 <a href="/">Home</a> |  '
                        " <a href='page2'>Page 2</a> | " 
                        " <a href='page3'>Page 3</a> | "
                        " <a href='page4'>Page 4</a> | "
                        " <a href='page5'>Page 5</a>"
                        )
def page2(request):
    return HttpResponse('page 2 <a href="/">Home</a> | '
                        "<a href='page1'>Page 1</a> | "
                        " <a href='page3'>Page 3</a> | "
                        " <a href='page4'>Page 4</a> |"
                        " <a href='page5'>Page 5</a>"
                        )
def page3(request):
    return HttpResponse('Page 3 <a href="/">Home</a> | '
                        "<a href='page1'>Page 1</a> | "
                        " <a href='page2'>Page 2</a> |"
                        " <a href='page4'>Page 4</a> |"
                        " <a href='page5'>Page 5</a>"
                        )
def page4(request):
    return HttpResponse('page 4 <a href="/">Back</a> | '
                        "<a href='page1'>Page 1</a> | "
                        " <a href='page2'>Page 2</a> | "
                        " <a href='page3'>Page 3</a> | "
                        " <a href='page5'>Page 5</a>"
                        )
def page5(request):
    return HttpResponse('Page 5 <a href="/">Home</a> | '
                        "<a href='page1'>Page 1</a> | "
                        " <a href='page2'>Page 2</a> | "
                        " <a href='page3'>Page 3</a> | "
                        " <a href='page4'>Page 4</a>"
                        )