from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import User,Pitch
from .. import db
from . forms import PitchForm
from flask_login import login_required


@main.route('/')
def index():
    """ View root page function that returns index page """

    title = 'Home- Welcome'
    return render_template('index.html', title = title)

@main.route('/category/pitch/new/', methods=['GET', 'POST'] )
@login_required

#route to page for posting pitch
def new_pitch():
    """ function to create the pitches """
    form = PitchForm()

    if form.validate_on_submit():
        content=form.content.data
        category_id=form.category_id.data

        ### clear content field after post
        form.content.data = ''

        new_pitch= Pitch(content=content,category_id= category_id)
        new_pitch.save_pitch()


    return render_template('new_pitch.html', form_pitch=form)

@main.route('/inteview_pitches/')
@login_required
def interview():
    '''
    View root page function that returns interview pitches
    '''
    title = 'Interviews'

    pitches= Pitch.get_pitches()

    return render_template('interview.html', title = title, pitches= pitches )
#pickup lines route
@main.route('/pick_up_line/')
def pick_up_line():
    '''
    View root page function that returns interview pitches
    '''
    title = 'Pick up lines'

    pitches= Pitch.get_pitches()

    return render_template('pick_up_line.html', title = title, pitches= pitches )

#promotions route
@main.route('/promotion/')
def promotion():
    '''
    View root page function that returns promotion pitches
    '''
    title = 'Promotion'

    pitches= Pitch.get_pitches()

    return render_template('promotion.html', title = title, pitches= pitches )

#product route
@main.route('/product/')
def product():
    '''
    View root page function that returns promotion pitches
    '''
    title = 'Promotion'

    pitches= Pitch.get_pitches()

    return render_template('product.html', title = title, pitches= pitches )

@main.route('/pitch/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_comment(id):
    '''
    Function that returns a list of comments for the particular pitch
    '''
    form = CommentForm()
    pitches = Pitches.query.filter_by(id=id).first()

    if pitches is None:
        abort(404)

    if form.validate_on_submit():
        comment_data = form.comment_id.data
        new_comment = Comments(comment_data=comment_data,
                               user_id=current_user.id, pitches_id=pitches.id)
        new_comment.save_comment()
        return redirect(url_for('.category', id=pitches.category_id))

    return render_template('comment.html', comment_form=form)


# Route for adding a new pitch
# @main.route('/category/pitch/new/<int:id>', methods=['GET', 'POST'])
# @login_required
# def new_pitch(id):
#     '''
#     Function to check Pitches form
#     '''
#     form = PitchForm()
#     #category = PitchCategory.query.filter_by(id=id).first()
#
#     if category is None:
#         abort(404)
#
#     if form.validate_on_submit():
#         actual_pitch = form.content.data
#         new_pitch = Pitches(actual_pitch=actual_pitch,
#                             user_id=current_user.id, category_id=category.id)
#         new_pitch.save_pitch()
#         return redirect(url_for('.category', id=category.id))
#
#     return render_template('new_pitch.html', pitch_form=form, category=category)

# Routes for displaying the different pitches
