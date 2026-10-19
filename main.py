# Working with Sets
from pyscript import display, document

grade_seven = {'Renzo Arce', 'Koby Baylon', 'Yciar Precones'}
grade_eight = {'Caleb Macachor', 'Thea Correa', 'Franco Garcia'}
grade_nine = {'Jeleen Gonzales', 'Rico Gozum', 'Jamielle Orduna'}
grade_ten = {'Aiva Suson', 'Maryam Ledesma', 'Zarina Perez'}

# Combine all grade levels
total_members = grade_seven | grade_eight | grade_nine | grade_ten
display(total_members, target="results")
display(f"Total number of members: {len(total_members)}", target="results")

def submit(event=None):
    first_name = document.getElementById("fname").value.strip().title()
    last_name = document.getElementById("surname").value.strip().title()

    new_member = first_name + " " + last_name
    grade_seven.add(new_member)
    total_members = grade_seven | grade_eight | grade_nine | grade_ten

    document.getElementById("results").innerHTML = ""
    display(total_members, target="results")
    display(f"Total number of members: {len(total_members)}", target="results")

    document.getElementById("fname").value = ""
    document.getElementById("surname").value = ""
