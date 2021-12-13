from flask import Blueprint, Flask, redirect, render_template, request
from models.owner import Owner

# import models and repos
# from models.vet import Vet
# import repositories.vet_repository as vet_repo
# import repositories.animal_repository as animal_repo
# import repositories.appointment_repository as appt_repo
import repositories.owner_repository as owner_repo


# set up blueprint
owners_blueprint = Blueprint("owners", __name__)

# INDEX
@owners_blueprint.route("/owners")
def owners():
    owners = owner_repo.select_all()
    return render_template("owners/index.html", all_owners = owners)

# VIEW
@owners_blueprint.route("/owners/<id>")
def view_owner(id):
    owner = owner_repo.select(id)
    return render_template("owners/view.html", owner=owner)

# NEW
@owners_blueprint.route("/owners/add")
def new_owner():
    return render_template("/owners/add.html")

# CREATE
@owners_blueprint.route("/owners", methods=["POST"])
def create_owner():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    owner = Owner(name, email, phone)
    owner_repo.save(owner)
    return redirect("/owners")


# EDIT



# UPDATE




# DELETE
@owners_blueprint.route("/owners/<id>/delete", methods=['POST'])
def delete_owner(id):
    owner_repo.delete(id)
    return redirect("/owners")