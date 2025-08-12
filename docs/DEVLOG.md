# EXO DEVLOG

July 18, 2025

    Session 1:
    Started designing the project with an LLM as I currently need help on designing a complete application from start
    to deployment, due to lack of experience. Will write the instructions the LLM gives on the INSTRUCTIONS.md file
    in order to keep them handy throught the learning journey. Will write here what I do within each building session.

    Started project with folder structure and empty files, including README.md, DEVLOG.md, STRUCTURE_EXPLANATION.md and INSTRUCTIONS.md. Feeling excited and confident on the path ahead. Currently fighting "scope creep" with the LLM.

July 19, 2025

    Session 1:
    Started prompting the LLM to write Task files, simulating real world, professional experience. 
    Added dependencies to project in addition to requirements.txt. Edited config.py, moving on to extensions.py. Became aware of The Twelve-Factor app 'ethos'(?) -> https://12factor.net/

July 23, 2025

    Session 1:
    Started with TASK_THREE.pdf step 4. Found out through LLM a new way to think about classes, especially ones that you import: 
    "A class is like a template for creating objects." Also, just learned to use '#' on .md as H1 'tags'. 😎

    Completed exo/app/auth/routes.py with full logic for registration, login and logout, including errors (using flash()!). 
    Initialized login_manager and wrote route to ensure protected routes and admin route(s). 
    General improvements to the structure and learned a little bit more of the "why's" regarding it. 
    Excited to continue working on this project and I am learning a LOT about application building!

    Completed exo/app/admin/routes.py. Had fun writing SQLAlchemy ORM syntax.

    Started with edition of templates/auth/login.html and templates/auth/register.html.

July 25, 2025

    Session 1:
    App runs! Edited fully base.html, still got progress to go. Need to add functionality to navbar depending user and 
    which page you are on. Got some hex color ideas from coolors.com. Started with style.css file. 
    Initialized flask-assets. Correctly defined routes.py on admin, auth and main folders. 
    Need to check if admin_required decorator fully works. But hey, app runs.

August 4, 2025

    Session 1:
    Took a 1 week + 2 day break, did code some stuff here and there but no 'power' sessions. With last push, 
    edited base.html thoroughly, added a new .css file for forms, particularly thinking on separating 
    the login form from the register form. The nav bar got updated, now will show options 
    if user logged in or not and if admin. Colors are cooler, will be editing them later on, but for now they look nice.
    User cannot register yet, and I need to create the admin account. Those are the next steps after I finish with forms.css.
    After, I will need to edit the styles on the approval_dashboard.html template. 
    Then after that will move on to TASK_FOUR.pdf 
    
    I'm having fun with the project, the self-imposed deadline approaches
    (September 1st, 2025). Let's see if life lets me finish it on or before the deadline! 
    Work has been intense lately, my general mood has been turning a little negative. 
    Also, quitting caffeine does have to do with the mood change, but did help a lot last time. 
    Let's see how the project goes!

August 10, 2025

    I've been thinking lately how much time I've spent, and how much I've learned byt just setting up the application,
    and creating the authentication routes/templates/etc. Definitely feels like a good step forward from CS50 week 9's 
    Flask project. 
    
    Love this line on admin/routes.py! 
        ```
        unapproved_users = {username : email for username, email in results}
        ```
    You can write a for loop in the same line, *inside* the initialization of a dictionary, who knew?!

    Admin can currently log in and log off. Can also access the admin_dashboard.html template. 
    I need to check next the register route and make it work.

    So far I'm still having fun. Just noticed, 21 days until deadline. Viene vieneeee 👾

    Update on caffeine quit -> It's going well, no more side effects. Bought a swiss-water method decaf one, 
    tastes very bad and was very expensive. Gabriel 1, Decaf company 1.

August 12, 2025

        Managed to make the admin_dashboard.html and admin/routes.py work together. 
        Admin will successfully see all the unapproved users in the user database and have the option to approve.
        Also, users can now register. Would need to change logic and create a "pending_approval.html" template for the user 
        before getting approved by admin. Big step tho! Success flash messages are still appearing red, 
        I thought I properly changed that with the update to style.css. In a later session I will check this.

        Currently tired, worked my final shift for this 'week', will go to sleep soon. I have a rehearsal tomorrow, will try to get at least 6hrs of sleep. Let's go!
