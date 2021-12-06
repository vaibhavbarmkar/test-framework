from deepdiff import DeepDiff
import logging,json

class HelperFunctions:

    @staticmethod
    def compare_jsons(obj_1, obj_2,ignore_order=True):
        logging.info("Starting function compare_jsons")
        diff = DeepDiff(obj_1,obj_2,ignore_order=ignore_order)
        if not diff:
            logging.info("Two Json Objects are equal")
            logging.info("Completed Json object comparision")
            return True
        else:
            logging.error("Two Json Objects are not equal " + str(diff))
            logging.info("Completed Json object comparision")
            return False

