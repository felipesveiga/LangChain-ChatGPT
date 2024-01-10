_configs = {
        'input_chain':{
            'template':'Write a short {language} function that will {task}',
            'input_variables':['language', 'task'],
            'output_key':'code'
            },
        'test_chain':{
            'template':'Write test for the following {language} code:\n{code}',
            'input_variables':['language', 'code'],
            'output_key':'test'
                },
        'main_chain':{
            'input_variables':['task', 'language'],
            'output_variables':['test', 'code']
                },
        'cli': {
            'arguments':['--language', '--task'],
            }
        }
