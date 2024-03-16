from abc import ABC, abstractmethod


class CommandHandler(ABC):
    @abstractmethod
    def add_record(self):
        pass

    @abstractmethod
    def find_record(self, search_term):
        pass

    @abstractmethod
    def delete_record_by_id(self):
        pass

    @abstractmethod
    def edit_record(self):
        pass

    @abstractmethod
    def show_all_records(self):
        pass

    @abstractmethod
    def add_note(self):
        pass

    @abstractmethod
    def delete_note(self):
        pass

    @abstractmethod
    def edit_note(self):
        pass

    @abstractmethod
    def show_notes(self):
        pass

    @abstractmethod
    def search_notes_by_tag(self, tag):
        pass

    @abstractmethod
    def sort_notes_by_tags(self, tag):
        pass

