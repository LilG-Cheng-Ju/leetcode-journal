import os
import urllib.parse

algorithms_path = "docs/algorithms" 
problems_path = "problems"

algorithm_markdown_file = "docs/README.md"
problem_markdown_file = "problems/README.md"

algorithms = sorted(os.listdir(algorithms_path))
problems = sorted([f for f in os.listdir(problems_path) if os.path.isdir(os.path.join(problems_path, f))])

with open(algorithm_markdown_file, "w") as f:
    f.write("# Algorithms\n\n")
    for algorithm in algorithms:
        algorithm_name = algorithm.replace(".md", "")
        encoded_algorithm = urllib.parse.quote(algorithm)
        algorithm_link = f"[{algorithm_name}](algorithms/{encoded_algorithm})"
        f.write(f"- {algorithm_link}\n")
        
with open(problem_markdown_file, "w") as f:
    f.write("# Problems\n\n")
    for problem in problems:
        encoded_problem = urllib.parse.quote(problem)
        problem_link = f"[{problem}]({encoded_problem})"
        f.write(f"- {problem_link}\n")

print("Markdown files updated successfully.")