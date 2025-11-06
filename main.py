from pyscript import display, document

def general_weighted_average(e):
    document.getElementById('student_info').innerHTML = ''
    document.getElementById('summary').innerHTML = ''
    document.getElementById('output').innerHTML = ''
    document.getElementById('status').innerHTML = ''

    subjects = ['Science', 'Math', 'English', 'Filipino', 'ICT', 'PE', 'SS', 'VE', 'TLE', 'CAT', 'Music']
    grades = []

    for sub in ['science', 'math', 'english', 'filipino', 'ict', 'pe', 'ss', 've', 'tle', 'cat', 'music']:
        grades.append(float(document.getElementById(sub).value))

    first_name = document.getElementById('first_name').value
    last_name = document.getElementById('last_name').value

    gwa = sum(grades) / len(grades)

    summary = "\n".join([f"{subjects[i]}: {grades[i]:.0f}" for i in range(len(subjects))])
    
    display(f"Name: {first_name} {last_name}", target="student_info")
    display(summary, target='summary')
    display(f"Your General Weighted Average is {gwa:.2f}", target='output')

    # Pass/Fail section
    status_div = document.getElementById("status")
    if gwa >= 75:
        status_div.innerHTML = "🎉 Congratulations! You Passed!"
        status_div.className = "pass"
    else:
        status_div.innerHTML = "❌ You Failed. Try harder next time."
        status_div.className = "fail"
