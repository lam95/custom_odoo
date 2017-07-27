{
    'name': 'Multiuser To-Do', 
    'description': 'Extend the To-Do app to multiuser.', 
    'author': 'Link Em',
    'depends': ['todo_app','mail'], 

    'data': [
        'views/todo_task.xml',
        'security/todo_access_rules.xml',
    ]
}