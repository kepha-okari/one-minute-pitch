from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import User,Pitch
from .. import db
from . forms import PitchForm
from flask_login import login_required


@main.route('/')
def index():
    """View root page function that returns index page"""

    title = 'Home- Welcome'
    return render_template('index.html', title = title)

@main.route('/category/pitch/new/', methods=['GET', 'POST'] )
@login_required
def new_pitch():
    """function to create the pitches"""
    form = PitchForm()

    if form.validate_on_submit():
        content=form.content.data
        category_id=form.category_id.data


        new_pitch= Pitch(content=content,cagory_id= category_id)
        new_pitch.save_pitch()

        #return redirect(url_for('.category', id=category.id))

    return render_template('new_pitch.html', form=form)


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
