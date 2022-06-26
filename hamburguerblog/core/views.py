from flask import render_template,request,Blueprint
from flask.templating import render_template

from hamburguerblog.models import BlogPost

core = Blueprint('core', __name__)

@core.route('/')
def index():
    page = request.args.get('page',1,type=Int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.dec()).paginate(page=page,per_page=10)
    return render_template('index.html',blog_posts=blog_posts)

@core.route('/info')
def info():
    return render_template('info.html')