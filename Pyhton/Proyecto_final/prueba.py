class Camper:
    def __init__(self, id, name, last_name, address, guardian, contact_numbers, status):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.address = address
        self.guardian = guardian
        self.contact_numbers = contact_numbers
        self.status = status

class TrainingRoute:
    def __init__(self, name, areas, max_capacity):
        self.name = name
        self.areas = areas
        self.max_capacity = max_capacity
        self.current_capacity = 0

class Test:
    def __init__(self, theoretical, practical):
        self.theoretical = theoretical
        self.practical = practical

class Module:
    def __init__(self, route, trainer, start_date, end_date, classroom):
        self.route = route
        self.trainer = trainer
        self.start_date = start_date
        self.end_date = end_date
        self.classroom = classroom
        self.scores = {}

class Trainer:
    def __init__(self, name, routes):
        self.name = name
        self.routes = routes

class CampusLands:
    def __init__(self):
        self.campers = []
        self.routes = []
        self.trainers = []
        self.modules = []

    def register_camper(self, camper):
        self.campers.append(camper)

    def create_training_route(self, name, areas, max_capacity):
        route = TrainingRoute(name, areas, max_capacity)
        self.routes.append(route)

    def assign_camper_to_route(self, camper, route):
        if route.current_capacity < route.max_capacity:
            route.current_capacity += 1
            # Asignar el camper a la ruta

    def register_test_score(self, camper, test_score):
        # Registrar la nota del examen
        if camper.status == "Inscrito":
            camper.status = "Aprobado" if (test_score.theoretical + test_score.practical) / 2 >= 60 else "Reprobado"

    def enroll_camper_in_module(self, camper, module):
        # Asignar el camper al módulo
        if module.route.current_capacity < module.route.max_capacity:
            module.route.current_capacity += 1
            module.scores[camper.id] = None

    def evaluate_performance(self, module):
        # Evaluar el rendimiento del camper en el módulo
        for camper_id, test_score in module.scores.items():
            if test_score:
                final_score = (test_score.theoretical * 0.3) + (test_score.practical * 0.6)
                if final_score < 60:
                    print(f"Camper {camper_id} tiene bajo rendimiento en el módulo {module.route.name}")

    def get_campers_in_status(self, status):
        # Listar campers en un estado específico
        return [camper for camper in self.campers if camper.status == status]

    def get_approved_initial_exam_campers(self):
        # Listar campers que aprobaron el examen inicial
        return [camper for camper in self.campers if camper.status == "Aprobado"]

    def get_working_trainers(self):
        # Listar entrenadores que están trabajando
        return [trainer for trainer in self.trainers if trainer.routes]

    def get_underperforming_campers(self):
        # Listar campers con bajo rendimiento
        return [camper for module in self.modules for camper, score in module.scores.items() if score and ((score.theoretical * 0.3) + (score.practical * 0.6)) < 60]

    def get_campers_and_trainer_for_route(self, route):
        # Listar campers y entrenador asociados a una ruta de entrenamiento
        campers = [camper for module in self.modules if module.route == route for camper, _ in module.scores.items()]
        trainer = [trainer for trainer in self.trainers if route in trainer.routes]
        return campers, trainer

    def get_module_results(self):
        # Mostrar resultados de los módulos (campers que aprobaron y perdieron)
        for module in self.modules:
            passed = sum(1 for score in module.scores.values() if score and ((score.theoretical * 0.3) + (score.practical * 0.6)) >= 60)
            failed = len(module.scores) - passed
            print(f"En el módulo {module.route.name} con entrenador {module.trainer.name}, {passed} campers aprobaron y {failed} campers perdieron.")
