def log_event(*events):
    if len(events) ==0:
        return 'No events to Log'
    for event in events:    
        if not isinstance(event,str):
            return 'Invalid event detected'

    for i in events:
        print(f'EVENT: {i}')