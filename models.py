class Part:
    """Деталь"""
    def __init__(self, part_id, name, supplier_id):
        self.part_id = part_id  # ID детали
        self.name = name  # Наименование детали
        self.supplier_id = supplier_id  # ID поставщика


class Supplier:
    """Поставщик"""
    def __init__(self, supplier_id, name):
        self.supplier_id = supplier_id  # ID поставщика
        self.name = name  # Наименование поставщика