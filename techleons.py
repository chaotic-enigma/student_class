def event_registration():    
    try:
        rsvp = 0
        events = []        
        technical_events = {1 : 'Gaming',
                            2 : 'Coding and Debugging',
                            3 : 'Hackathon',
                            4 : 'Web-Designing',
                            5 : 'Treasure Hunt',
                            6 : 'Dumcharades'}
        
        print('Below are the details for registration in techleons')        
        for keys,values in technical_events.items():
            print('\t' + str(keys) + ' --> ' + str(values))
            
        while rsvp < len(technical_events)/2:
            raw = input('Enter your choice: ')
            
            for i,k in technical_events.items():
                if raw in list(technical_events.keys()):
                    events.append(technical_events[raw])
                    break
                elif raw < 1 or raw > len(technical_events):
                    print('The option which you have chosen is unobservant. \nPlease select the valid option.')
                    break
                else:
                    print('Input not understood')
                    break
                    
            response = input('Interested in another event? (y/n)')            
            if response == 'y':
                rsvp += 1
            elif response == 'n':
                print('Hope you are happy with what you have selected.\n')
                return list(set(events))
                break
            else:
                print('Input not understood.\n')
                return list(set(events))
                break
            if rsvp >= 3:
                print('You can only choose atmost 3 events.\n')
                return list(set(events))
                break                
    except (NameError, SyntaxError):
        print('Please check your input.\n')
        return list(set(events))