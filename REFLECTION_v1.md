# Project Reflection: Refactoring `processCustomer`

### 1. How did you achieve functional cohesion? Which routines did you extract?
The initial routine exhibited bad procedural and logical cohesion because it performed validation, mathematical calculation, string construction, and I/O tasks within a single block. 

To achieve functional cohesion, the routine was broken down so that every function or procedure handles exactly one single task. The following highly focused sub-routines were extracted:
* `validateInputs`: Responsible solely for checking constraints (no negative numbers, bounds checking, and type confirmation).
* `calculateSum`: Strictly loops over and adds up array/list contents.
* `determineDiscountRate`: Converts type identifiers into numerical multipliers cleanly without computing totals.
* `calculateTotal`: Performs the arithmetic deduction for discounts.
* `formatCustomerMessage`: Converts the context state into user-facing output blocks.

Following standard clean code architecture, computational tasks returning values are named via noun phrases (`calculateSum`, `determineDiscountRate`), while actions modifying state or producing side effects are named using `verb+object` syntax (`validateInputs`, `printMessage`).

### 2. What parameter passing issues did you encounter (e.g., d modified but not returned)?
In the original block, the variable argument `d` was reassigned locally at the bottom (`d = total;`). Because both Java and Python pass primitives/reassignments by-value, local reassignments inside a function's stack frame do not propagate back up to the calling scope. In the legacy version, the updated calculation to `d` was lost entirely upon exit. 

To resolve this limitation cleanly, the design was changed from tracking an implicitly updated state reference to an explicit return assignment. The calculated absolute price is now naturally passed back to the caller using a standard `return` statement.

### 3. How would the d update behave differently if the language used pass-by-value-result?
If the runtime compiler executed on pass-by-value-result parameters (such as inside Ada structures):
1. **At invocation (Copy-in):** A copy of the caller’s original local variable passed as argument `d` would be generated inside the execution scope.
2. **During processing:** The function would execute normally using this isolated local copy.
3. **At method exit (Copy-out):** The final updated state assigned to the formal parameter `d` inside the local scope would get systematically written over and assigned back into the memory address of the original argument variable.

Consequently, unlike the pass-by-value constraint seen in Java or Python, under a pass-by-value-result mechanism, the calling method's outer variable would be altered automatically when the function finishes execution.
