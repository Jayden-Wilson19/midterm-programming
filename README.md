# CMPSC 202 - Midterm Programming Assignment

Name: Jayden Wilson

**Instructions**: Complete the exercise below. Open book, open notes, any tools allowed (except submitting another student's work). Due tonight (10/6) at 11:59pm.

**Submission**: Fork this repository and invite your professor (username: bcmullins) to the repository. To submit, push your code to your forked repository. Make sure to include your name in the README file.

You have been provided with a starter Python file (`midterm_starter.py`). This file contains two fully implemented algorithms that solve the exact same problem: finding if an array contains duplicate values.

The file also contains a `flawed_benchmark()` function. The developer who wrote this benchmark made several severe methodological errors, making the printed timing results completely unreliable for comparing the asymptotic growth of these two algorithms.

**Your tasks**: 

1. Rewrite the `flawed_benchmark()` function to provide a robust empirical comparison of the two algorithms. List the methodological errors in the original benchmark and explain how you fixed them. Your benchmark should demonstrate the scaling behavior of the two algorithms across multiple input sizes.

- Only 5 trials were used: A small number of trials makes the results more vulnerable to random sstem activity and timing noise. I fixed it b increasing the number from 5 to 7

- Timing order could introduce bias: If the same algorithm always runs first, effects such as CPU/cache behavior can systematically favor one implementation. I fixed it by creating a revised benchmark that alternates the execution bewtween trials.

- The function name: The name itself stated it was flawed, simply renaming it to benchmark_duplicates()

- No correctness verification: A timing comparison is meaningless if one implementation produces an incorrect result. Fixing this so each run checks that the algorithm returns False duplicate-free input and raises an error otherwise.

- A limited description: It never explained clearly why the chosen methodology produces meaningless measurements. I instead revised a docstring that explaines the algorithm receives identical inputs, are tested at increasing sizes, and use repeated median measurements.

- Small inputs can make timing noise significant: For fast algorithms, execution times on small inputs may be short that normal system fluctuations dominate the measurement. 

2. Run the empirical comparion and plot the results using a plotting library of your choice (e.g., `matplotlib`, `seaborn`, etc.). Include the plot in your submission called `results.png`. Be sure to label your axes and include a legend.



