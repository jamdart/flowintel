from flask import Blueprint, render_template, redirect, jsonify, request, flash
from flask_login import login_required, current_user
from . import calendar_core as CalendarModel
from ..db_class.db import Org, Case_Org
from ..decorators import editor_required

calendar_blueprint = Blueprint(
    'calendar',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@calendar_blueprint.route("/", methods=['GET'])
@login_required
def calendar():
    """Calendar view"""
    return render_template("calendar.html")


@calendar_blueprint.route("/get_task_month", methods=['GET'])
@login_required
def get_task_month():
    """Calendar info"""

    data_dict = dict(request.args)
    date_month = data_dict["date"]
    if date_month:
        tasks_list = list()
        tasks_month = CalendarModel.get_task_month_core(date_month, current_user)
        for task in tasks_month:
            tasks_list.append(task.to_json())

        return {"tasks": tasks_list}
    return {"message": "No date"}