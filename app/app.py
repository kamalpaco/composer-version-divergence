import os
import json
import matplotlib.pyplot as plt
import networkx as nx
import sys

def parse_composer_json(file_path):
    with open(file_path) as f:
        data = json.load(f)
        return data

def create_dependency_graph(files):
    graph = nx.DiGraph()
    for file in files:
        data = parse_composer_json(file)
        package_name = data.get('name', '')
        package_version = data.get('version', '')
        graph.add_node(package_name, version=package_version)

        require = parse_composer_json(file).get('require', {})
        for dependency, version_constraint in require.items():
            graph.add_edge(package_name, dependency, version_constraint=version_constraint)
    
    return graph

def visualize_dependency_graph(graph, output_file):
    pos = nx.spring_layout(graph)
    plt.figure(figsize=(24, 16))
    nx.draw_networkx(graph, pos, node_size=1000, node_color='lightblue', font_size=10, font_weight='bold', with_labels=True)
    edge_labels = nx.get_edge_attributes(graph, 'version_constraint')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=12, label_pos=0.5, font_color='red')
    plt.title("Divergence of Library Versions")
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()

if __name__ == "__main__":
    directory = "projects/"
    
    if not os.path.isdir(directory):
        print("Advertencia: El directorio proporcionado no existe.")
        print("Por favor, ejecute el script nuevamente y proporcione un directorio válido.")
        sys.exit(1)

    composer_files = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.json')]

    if not composer_files:
        print("Advertencia: No se encontraron archivos composer.json en el directorio proporcionado.")
        print("Por favor, coloque los archivos composer.json en el directorio y ejecute el script nuevamente.")
        sys.exit(1)

    output_file = "dependency_graph.png"
    dependency_graph = create_dependency_graph(composer_files)
    visualize_dependency_graph(dependency_graph, output_file)
    print(f"El gráfico de dependencias se ha guardado en {output_file}.")