"""Reusable unique string gatherer. Returns unique string values only, with optional"""


class ListGatherer:

    def __init__(self):
        self.args_dict = {}

    def _not_in_args(self, check):
        for arg_list in self.args_dict.values():
            if check in arg_list:
                return False
        return True

    def run(self, header: str = '', *args: list) -> list:
        """Gathers input from user, split by newline. Runs until blank line submitted. Checks input
        value against itself and lists provided in args to ensure unique and allowed values only"""

        self.args_dict.clear()
        for ndx, arg in enumerate(args):
            self.args_dict[ndx] = arg

        gathered = []

        print("\n" + header + "\n")

        prompt: str = None
        while prompt != '':
            prompt = input('> ').lower().strip()
            if prompt != '' and prompt not in gathered and self._not_in_args(prompt):
                gathered.append(prompt)

        return gathered


# gatherer = ListGatherer().run
# head = "sample words to display"
# print(gatherer(head, ['1', '2', '3', '4', '5'], ['6', '7', '8', '9', '10']))
