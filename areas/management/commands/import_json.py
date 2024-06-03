import json
from django.core.management.base import BaseCommand
from nodes.models import Node
from edges.models import Edge
from areas.models import Area
from django.template.defaultfilters import slugify


class Command(BaseCommand):
    help = "Import nodes and edges from a JSON file into the database"

    def add_arguments(self, parser):
        parser.add_argument("json_file", type=str, help="The JSON file to import")

    def handle(self, *args, **kwargs):
        json_file = kwargs["json_file"]
        with open(json_file, "r") as file:
            data = json.load(file)

        area_id = 5
        area = Area.objects.get(id=area_id)

        # Import nodes
        for node_data in data["nodes"]:
            slug = slugify(node_data["id"])
            node, created = Node.objects.get_or_create(
                slug=slug,
                defaults={
                    "title": node_data["id"],
                    "area": area,
                    "x": node_data["x"],
                    "y": node_data["y"],
                    "owner_id": 1,  # Replace with the appropriate owner ID
                },
            )
            if not created:
                # Update existing node if needed
                node.x = node_data["x"]
                node.y = node_data["y"]
                node.save()

        # Import edges
        for edge_data in data["edges"]:
            try:
                source_node = Node.objects.get(title=edge_data["source"], area=area)
                target_node = Node.objects.get(title=edge_data["target"], area=area)
                Edge.objects.get_or_create(source=source_node, target=target_node)
            except Node.DoesNotExist as e:
                self.stdout.write(self.style.ERROR(f"Node not found: {e}"))
                continue

        self.stdout.write(self.style.SUCCESS("Successfully imported nodes and edges"))
