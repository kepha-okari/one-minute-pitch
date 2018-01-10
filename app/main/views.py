
from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import User,Pitch,Comments,PitchCategory
from .. import db
from . forms import PitchForm, CommentForm
from flask_login import login_required,current_user

#display categories on the landing page
@main.route('/')
def index():
    """ View root page function that returns index page """

    category = PitchCategory.get_categories()

    title = 'Home- Welcome'
    return render_template('index.html', title = title, categories=category)



#Route for adding a new pitch
@main.route('/category/new-pitch/<int:id>', methods=['GET', 'POST'])
@login_required
def new_pitch(id):
    ''' Function to check Pitches form '''
    form = PitchForm()
    category = PitchCategory.query.filter_by(id=id).first()

    if category is None:
        abort(404)

    if form.validate_on_submit():
        content = form.content.data
        new_pitch= Pitch(content=content,category_id= category.id,user_id=current_user.id)
        new_pitch.save_pitch()
        return redirect(url_for('.index', id=category.id))

    return render_template('new_pitch.html', pitch_form=form, category=category)

#view pitches
@main.route('/view-pitch/<int:id>', methods=['GET', 'POST'])
@login_required
def view_pitch(id):
    '''Function the returns a single pitch for comment to be added'''

    pitches = Pitch.query.get(id)

    if pitches is None:
        abort(404)

    return render_template('view-pitch.html', pitches=pitches)




# @main.route('/category/pitch/new/', methods=['GET', 'POST'] )
# @login_required
# #route to page for posting pitch
# def new_pitch(id):
#     """ function to create the pitches """
#     form = PitchForm()
#
#     if form.validate_on_submit():
#         content=form.content.data
#         category_id=form.category_id.data
#
#         ### clear content field after post
#         form.content.data = ''
#
#         new_pitch= Pitch(content=content,category_id= category_id)
#         new_pitch.save_pitch()
#
#
#     return render_template('new_pitch.html', form_pitch=form)


@main.route('/pitch/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_comment(id):
    '''
    Function that returns a list of comments for the particular pitch
    '''
    form = CommentForm()
    pitches = Pitch.query.filter_by(id=id).first()
    #
    if pitches is None:
         abort(404)

    if form.validate_on_submit():
        opinion = form.opinion.data
        new_comment = Comments(opinion=opinion, user_id=current_user.id, pitches_id=pitches.id)
        new_comment.save_comment()
        return redirect(url_for('.new_pitch', id=pitches.id))

    return render_template('comment.html', comment_form=form)



#Routes for displaying the different pitches
