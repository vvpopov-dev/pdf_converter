from src.handlers.start import start
# from src.handlers.pdf import pdf_handler
# from src.handlers.word import word_handler
from src.handlers.merge import merge_pdf_handler
from src.handlers.back import back_to_main
from src.handlers.settings import change_language, set_language
from src.handlers.support import support, support_message
from src.handlers.word_to_pdf import word_to_pdf_handler
from src.handlers.pdf_to_word import pdf_to_word_handler


__all__ = [
    "start", "merge_pdf_handler", "back_to_main", 
    "settings", "change_language", "set_language", 
    "support", "support_message", "word_to_pdf_handler", 
    "pdf_to_word_handler"
    ]
