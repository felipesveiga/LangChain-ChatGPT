_configs = {
    'functions':{
        'database':'../../assets/06_db.sqlite',
        '_list_tables':{
                'execute':{
                '__sql':'SELECT name FROM sqlite_master WHERE type=\'table\';'
                }
        },
        'describe_tables':{
            'execute':{
                '__sql':'SELECT name FROM sqlite_master WHERE type=\'table\' AND name IN ({tables});'
            }
        }
    }
}