### CHAPTER 9: Mediation — The Search for a Mechanism

**Core Claim:** Direct and indirect effects cannot be defined using interventions (do-operators) alone; they require counterfactual definitions. The "mediation formula" (Pearl 2001) provides the first nonparametric, non-linear definition of natural direct and indirect effects and makes them estimable from observational data. The Baron-Kenny regression approach, though enormously influential, is valid only in linear models and fails with interactions.

**Supporting Evidence:**
- Scurvy history: doctors confused the mediator (thought it was acidity; was actually vitamin C) and nearly destroyed a century of knowledge
- Berkeley admissions paradox: gender appears to hurt women in aggregate but help them department by department — resolved as Simpson's paradox where department is a mediator
- Crossgull's counter-example: state-of-residence as a collider between department and outcome — showing the mediation fallacy (conditioning on mediator instead of holding it constant)
- Barbara Birx (1926): first path diagram outside Wright's work, first warning against collider bias, preceded Duncan and Blalock by 40 years
- Chicago "Algebra for All": direct effect = +2.7 points, indirect effect through classroom environment = −2.3 points, net ≈ 0
- Smoking gene: NIE ≈ +1-3% (gene barely increases cigarettes/day); NDE large and positive for smokers; interaction between gene and smoking is the real story

**Logical Method:** Historical + formal. Pearl shows that the conceptual problem (what do direct/indirect effects mean outside linear models?) was unresolved for 75 years, then derives the mediation formula as the solution.

**Logical Gaps:**
- The mediation formula requires no confounding between mediator and outcome (conditional on treatment). This assumption is very strong and often unverifiable. Pearl acknowledges it but presents it as a condition to check, not as a fundamental limitation.
- The Algebra for All analysis (Hong's study) uses a "variation of the mediation formula" — Pearl credits this but doesn't verify that the assumption of no mediator-outcome confounding holds for classroom environment.
- The tourniquet example is honest (null result, probably due to conditioning on survival-to-hospital) but Pearl is speculating about the mechanism. He has no data on prehospital mortality.

**Methodological Soundness:** The mediation formula's derivation is correct. The Birx historiography is accurate and underappreciated. The Chicago Algebra for All analysis is a strong real-world validation. The tourniquet analysis is honest about what the data can and cannot show.

---
