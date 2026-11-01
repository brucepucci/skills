# Standards smell baseline

Fowler code smells (*Refactoring*, ch. 3) supplement documented standards:

- **The repo overrides.** Where a documented rule endorses something the baseline would flag, suppress the smell.
- **Always a judgement call.** Smells are labelled heuristics ("possible Feature Envy"), not mandatory violations or blockers by themselves.
- Skip findings already enforced by tooling.

Pass this entire baseline to the Standards reviewer:

- **Mysterious Name**: a function, variable, or type whose name doesn't reveal what it does or holds. Rename it; if no honest name comes, the design is murky.
- **Duplicated Code**: the same logic shape appears in multiple hunks or files. Extract the shared shape.
- **Feature Envy**: a method reaches into another object's data more than its own. Move the method onto the data it envies.
- **Data Clumps**: the same fields or parameters keep travelling together. Bundle them into one type.
- **Primitive Obsession**: a primitive stands in for a domain concept deserving its own type. Introduce that small type.
- **Repeated Switches**: the same type-dependent cascade recurs. Use polymorphism or one shared map.
- **Shotgun Surgery**: one logical change forces scattered edits. Gather what changes together.
- **Divergent Change**: one module changes for unrelated reasons. Split by reason to change.
- **Speculative Generality**: abstraction or hooks serve needs the spec does not have. Remove until there is a real need.
- **Message Chains**: callers depend on long navigation chains. Hide the walk behind an appropriate interface.
- **Middle Man**: a class/function mostly delegates onward. Consider calling the real target directly.
- **Refused Bequest**: a subclass ignores most inherited behavior. Prefer composition.
