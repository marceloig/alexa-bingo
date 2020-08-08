import logging
import ask_sdk_core.utils as ask_utils
import boto3

from boto3.session import Session
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class SortNumberIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("SortNumberIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
                      
        speak_output = "Numero 9"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )
