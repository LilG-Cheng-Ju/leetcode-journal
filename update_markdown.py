import os
import urllib.parse

algorithms_path = "docs/algorithms" 
problems_path = "problems"

algorithm_markdown_file = "docs/README.md"
problem_markdown_file = "problems/README.md"

algorithms = sorted(os.listdir(algorithms_path))
problems = sorted([f for f in os.listdir(problems_path) if os.path.isdir(os.path.join(problems_path, f))],
                  key=lambda x: int(x.split(".")[0]))

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
        problem_path = os.path.join("problems", problem)
        
        readme_file = None
        for readme_name in ["README.md", "readme.md"]:
            readme_path = os.path.join(problem_path, readme_name)
            if os.path.exists(readme_path):
                readme_file = readme_path
                break

        if readme_file:
            with open(readme_file, "r") as readme:
                first_line = readme.readline().strip()
                problem_name = first_line.lstrip('#').strip()
        else:
            problem_name = problem.replace(".md", "")
            
        encoded_problem = urllib.parse.quote(problem)
        problem_link = f"[{problem_name}]({encoded_problem})"
        f.write(f"- {problem_link}\n")

print("Markdown files updated successfully.")