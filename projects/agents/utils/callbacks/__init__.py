from utils.callbacks.callbacks import ChatModelStartCallback

_configs_boxen = {
    'system':{
        'color':'yellow'
    },
    'human':{
        'color':'green'
    },
    'ai-function':{
        'text':'Running tool {tool} with args {args}',
        'color':'cyan'
    },
    'ai':{
        'color':'blue'
    },
    'function':{
        'color':'purble'
    },
    'else':{
        'color':''
    }
}