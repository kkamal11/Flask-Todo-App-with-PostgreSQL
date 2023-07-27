from flask import current_app as app
from flask import render_template, redirect, request, flash
from flask_security import auth_required
from flask_login import current_user
from application.database import db
from models.model import Todos

@app.route("/", methods=["GET", "POST"])
@auth_required('session')
def home():
    user = current_user
    if request.method == 'GET':
        todos = user.todos
        num_completed = sum([1 if todo.completed else 0 for todo in todos])
        return render_template("index.html", todos=todos, num_completed=num_completed)
    else:
        task_name = request.form.get('task_name', None)
        if task_name:
            task = Todos(
                task=task_name,
                completed=False
            )
            user.todos.append(task)
            db.session.commit()
            todos = user.todos
            num_completed = sum([1 if todo.completed else 0 for todo in todos])
            flash(message="Woohoo - Task added successfully!", category="success")
            return render_template("index.html", todos=todos, num_completed=num_completed)
        else:
            flash(message="Task cannot be empty. Please enter it in the box above.", category="error")
            return redirect("/")

@app.route("/update/<int:task_id>")
@auth_required('session')
def update_task_status(task_id):
    user = current_user
    if user:
        todos = user.todos
        for todo in todos:
            if todo.id == int(task_id):
                todo.completed = not todo.completed
                db.session.commit()
                return redirect("/")
    else:
        return redirect("/")

@app.route("/delete/<int:task_id>")
@auth_required('session')
def delete_tasks(task_id):
    user = current_user
    if user:
        todos = user.todos
        for todo in todos:
            if todo.id == int(task_id):
                db.session.delete(todo)
                db.session.commit()
                return redirect("/")
    else:
        return redirect("/")

@app.route("/delete")
@auth_required('session')
def delete_all_tasks():
    user = current_user
    if user:
        todos = user.todos
        for todo in todos:
            db.session.delete(todo)
            db.session.commit()
        return redirect('/')
    return redirect('/')

@app.route("/marks-as-complete")
@auth_required('session')
def marks_all_as_complete():
    user = current_user
    if user:
        todos = user.todos
        for todo in todos:
            todo.completed = True
            db.session.commit()
        return redirect('/')
    else:
        return redirect("/")