import view
import logger
import model

def run():
    mode = view.action()
    if mode == '1':
        base = logger.get_data()
        data = view.cont_to_search()
        model.search(base, data)
    if mode == '2':
        result = view.new_contact()        
        logger.new_entry(result)
