# Before/After: Plain EC English and the hard language gate

## 1. Software and administrative metaphors

### Before

> The optimization engine orchestrates a menu of refinement operators and uses inferred provenance to regulate archive admission.

### After

> The algorithm selects among several local-search operators and uses the estimated source of each solution to decide whether that solution enters the archive.

### Why

The revision names the actual operations. It does not ask the reader to interpret an engine, a menu, provenance, or admission as algorithm concepts.

## 2. Repeated stock contrast

### Before

> The method uses variable grouping rather than full-dimensional updates. It updates the archive every ten generations rather than every generation.

### After

> The method updates one group of variables at a time while keeping the other variables fixed. The archive is updated every ten generations.

### Why

The contrast is rebuilt as direct technical statements. The second sentence needs no contrast phrase at all.

## 3. Standard DE terminology

### Before

> It is worth noting that the proposed optimization engine leverages the target vector and the donor vector to facilitate the generation of a trial vector.

### After

> The algorithm generates a trial vector from the target and donor vectors.

### Why

`Trial vector` is standard DE terminology and remains unchanged. The surrounding metadiscourse and software metaphor are removed.

## 4. Abstract promotion

### Before

> In the realm of large-scale optimization, the proposed method harnesses intricate variable interactions to unlock seamless convergence.

### After

> The proposed method uses variable interactions in large-scale optimization.

### Why

The original supplies no evidence for seamless convergence, so the promotional claim is removed. No new mechanism or performance result is added.

## 5. Evidence must remain intact

### Before

> Rather than proving universal superiority, the results in Table II show that our algorithm reduces exact evaluations by 38% compared with its rival [12], although the mean accuracy was 1.2 points lower on the multimodal instances.

### After

> Table II shows that our algorithm reduces exact evaluations by 38% compared with [12]. On the multimodal instances, however, its mean accuracy was 1.2 points lower.

### Why

The numerical result, citation, comparison, and negative result are all preserved. Only the framing and wording change.
