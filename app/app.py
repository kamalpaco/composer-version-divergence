import os
import json
import matplotlib.pyplot as plt
import networkx as nx
import sys

def parse_composer_json(file_path):
    with open(file_path) as f:
        data = json.load(f)
        package_name = data.get('name', '')
        package_version = data.get('version', '')
        return package_name, package_version

def create_dependency_graph(files):
    graph = nx.DiGraph()
    for file in files:
        package_name, package_version = parse_composer_json(file)
        graph.add_node(package_name, version=package_version)

        require = parse_composer_json(file).get('require', {})
        for dependency, version_constraint in require.items():
            graph.add_edge(package_name, dependency, version_constraint=version_constraint)
    
    return graph

def visualize_dependency_graph(graph):
    pos = nx.spring_layout(graph)
    plt.figure(figsize=(12, 8))
    nx.draw_networkx(graph, pos, node_size=1000, node_color='lightblue', font_size=10, font_weight='bold', with_labels=True)
    edge_labels = nx.get_edge_attributes(graph, 'version_constraint')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=8)
    plt.title("Divergence of Library Versions")
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    # Obtener el directorio de archivos composer.json de la línea de comandos
    if len(sys.argv) < 2:
        print("Advertencia: No se proporcionó un directorio para evaluar.")
        print("Por favor, ejecute el script nuevamente y proporcione un directorio válido.")
        sys.exit(1)

    
    if not os.path.isdir(directory):
        print("Advertencia: El directorio proporcionado no existe.")
        print("Por favor, ejecute el script nuevamente y proporcione un directorio válido.")
        sys.exit(1)

    composer_files = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.json')]

    if not composer_files:
        print("Advertencia: No se encontraron archivos composer.json en el directorio proporcionado.")
        print("Por favor, coloque los archivos composer.json en el directorio y ejecute el script nuevamente.")
        sys.exit(1)

    dependency_graph = create_dependency_graph(composer_files)
    visualize_dependency_graph(dependency_graph)
