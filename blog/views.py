from django.shortcuts import render

def post_list(resquest):
    return  render(resquest, 'blog/post_list.html', {})
