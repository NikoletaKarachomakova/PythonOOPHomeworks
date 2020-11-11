from DocumentManagement.topic import Topic
from DocumentManagement.category import Category
from DocumentManagement.document import Document


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        for cat in self.categories:
            if cat.id == category_id:
                cat.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        for t in self.topics:
            if t.id == topic_id:
                t.topic = new_topic
                t.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        for d in self.documents:
            if d.id == document_id:
                d.file_name = new_file_name

    def delete_category(self, category_id):
        self.delete_by_id(category_id, self.categories)

    def delete_topic(self, topic_id):
        self.delete_by_id(topic_id, self.topics)

    def delete_document(self, document_id):
        self.delete_by_id(document_id, self.documents)

    def delete_by_id(self, del_id, from_list):
        for obj in from_list:
            if obj.id == del_id:
                from_list.remove(obj)

    def get_document(self, document_id):
        for doc in self.documents:
            if doc.id == document_id:
                return doc

    def __repr__(self):
        str_docs = [str(doc) for doc in self.documents]
        return "\n".join(str_docs)
