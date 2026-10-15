"""Public editorial summary of the private Incident Lab project; no runtime data."""

PROJECT = dict(
    slug='incident-lab', title='Incident Lab: investigating ML service failures',
    kind='Personal engineering project · 2026', category='engineering research',
    tags='Python, FastAPI, SQLite, OpenTelemetry, LLM evaluation, GitHub Actions',
    summary='An evidence-first AI workbench that compares rules and model hypotheses, preserves failed attempts, and makes recovery testable.',
    problem='An incident explanation can sound convincing while mixing services or citing evidence that does not support the diagnosis. Engineers need to inspect the observations, understand uncertainty and recover safely when a provider or worker fails.',
    contribution='I designed and built a local investigation workbench, a separate durable worker, a controlled fault-injection lab and a frozen evaluation workflow. This is solo, AI-assisted engineering: architecture decisions, implementation, failure analysis and delivery, with independent human review still pending.',
    approach='The application validates immutable observation snapshots, compares a rules baseline with a bounded model call, and checks the returned categories and citations. The model selects hypotheses and references; application code renders factual statements from the cited records. A separate controller and evaluator retain fault labels outside investigator input.',
    result='The v0.3.2 delivery passed 134 Python tests, JavaScript checks and clean Windows/Linux CI, including wheel installation outside the checkout. The portable demo preserves 36 synthetic observation windows and 72 saved report attempts: 64 completed and eight failed. Saved playback needs no provider key.',
    limitation='A local, single-user research workbench, not a production incident responder. Evaluations cover small, known synthetic failure families; controls include abstentions. The model has not demonstrated an advantage over the rules baseline. Shared support predicates constrain both approaches. Independent technical review and a physical second-PC check are deferred. No team-management experience is claimed.',
    source='https://www.linkedin.com/in/amit-tech/',
    source_label='Request a technical walkthrough',
    status='v0.3.2 delivered · source and demo private', diagram='incident',
    reviewed='15 October 2026',
)


def art():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 240" role="img" aria-label="Conceptual incident workflow: observations, validation, hypotheses and cited evidence"><rect width="440" height="240" fill="#e0ece7"/><g fill="#f7f7f2" stroke="#54767a" stroke-width="2"><rect x="30" y="70" width="95" height="100" rx="8"/><rect x="172" y="84" width="96" height="72" rx="8"/><rect x="315" y="50" width="95" height="140" rx="8"/></g><g fill="none" stroke="#116853" stroke-width="3"><path d="M125 120H172m-9-7 9 7-9 7M268 120H315m-9-7 9 7-9 7M49 92H105M49 112H96M49 132H105M49 152H82M195 121l16 15 34-34M333 76H389M333 96H381M333 116H391M333 157H374"/></g><circle cx="385" cy="157" r="10" fill="#116853"/><path d="m380 157 4 4 7-9" fill="none" stroke="#fff" stroke-width="2"/></svg>'''


def overview():
    return '''<div class="incident-flow" aria-label="Implemented investigation flow"><p class="eyebrow">From observation to review</p><ol><li><strong>Immutable snapshot</strong><span>Normalized signals and hashed source references.</span></li><li><strong>Bounded investigation</strong><span>Rules baseline plus one model call; omissions disclosed.</span></li><li><strong>Validated report</strong><span>Supported citations, source-rendered facts and visible failures.</span></li></ol><p class="fine">Architecture summary, not a live investigation.</p></div>'''


def featured():
    return '''<article class="featured incident-feature"><div class="featured-copy"><p class="eyebrow">Latest build · AI systems engineering · 2026</p><h3>Investigate the failure.<br>Keep the evidence.</h3><p>Incident Lab connects bounded AI investigation with durable jobs, citation checks and recovery drills. Every attempt stays visible, including the ones that fail.</p><div class="tags"><span>Python / FastAPI</span><span>System design</span><span>LLM evaluation</span></div><a class="textlink" href="projects/incident-lab.html">Explore Incident Lab ↗</a></div>'''+overview()+'''</article>'''


def details():
    return '''<h2>Architecture decisions</h2><ul>
<li><strong>A modular backend and one worker.</strong> FastAPI and SQLite keep state transitions inspectable. Leases fence stale writes; idempotency links duplicate submissions to the same job. This is a local persistence boundary, not distributed availability.</li>
<li><strong>A bounded model contract.</strong> Provider input is limited to 40 records and 10,000 serialized characters. Fixed signal mappings and opaque aliases replace raw log text. Groq was tested live; OpenAI remains an optional adapter without live verification.</li>
<li><strong>Evidence before fluent narration.</strong> Schema, citation and domain-support checks reject unsupported outputs. Exact observation values and timestamps come from source records. Citation correctness does not prove causality.</li>
<li><strong>Recovery without silent retries.</strong> HTTP 429 retains the failed attempt and persists a provider cooldown. Later queued work waits; rules can progress. Cancellation, process restart, backup/restore and unfinished-job quarantine are exercised with simulated providers.</li>
<li><strong>A separate evaluation boundary.</strong> A fault controller exercises an OpenTelemetry workload and a small trained ML service over HTTP. Scenario labels stay with the evaluator. The host worker does not inherit the separate rules container’s network isolation.</li>
</ul>
<h2>Frozen evaluation results</h2>
<div class="table-scroll"><table><caption>Separate synthetic campaigns · 14 October 2026</caption><thead><tr><th scope="col">Campaign</th><th scope="col">AI workflow</th><th scope="col">Rules baseline</th></tr></thead><tbody>
<tr><th scope="row">Original v0.3 · ML services</th><td>5/9</td><td>9/9</td></tr>
<tr><th scope="row">Original v0.3 · generic services</th><td>6/9</td><td>9/9</td></tr>
<tr><th scope="row">Later v0.3.1 · ML services</th><td>9/9</td><td>9/9</td></tr>
<tr><th scope="row">Later v0.3.1 · generic services</th><td>8/9</td><td>9/9</td></tr>
</tbody></table></div>
<p>Each denominator contains all nine scheduled windows, including failed attempts and controls. A match can be a supported fault hypothesis or an expected abstention; this is not fault-detection accuracy. The later generic campaign retained one HTTP 429 rejection. The original results were preserved.</p>
<p>The later campaigns followed diagnostic and citation-prompt changes. They are separate runs on known synthetic families, not independent proof of improvement. The v0.3.2 cooldown and delivery work introduced no new diagnosis-quality score.</p>
<h2>What the demonstration shows</h2>
<ol><li>Compare a saved ML contract-mismatch report with the rules baseline and follow a factual claim to its cited observation.</li><li>Inspect a healthy or recovery control that abstains, then open a failed attempt and its safe diagnostic category.</li><li>Run a simulated cooldown drill: retain the original 429, complete rules during the hold, cancel queued work and resume one later job after expiry.</li><li>Restore a verified backup and explain the boundary between a saved replay, a simulated operational test and a fresh provider call.</li></ol>
<p>Source and the portable release are private. A walkthrough is available on request; this public page is an editorial case study, not a hosted app or a public download. The demo includes no provider credentials, raw telemetry or employer data. No live model call is made by this website.</p>
<h2>Verified delivery</h2><p>Clean Windows and Linux CI passed for release source c28f5be. Package installation, browser playback, backup restoration and the mock cooldown drill were checked. The original evaluation files and v0.3.0 bundle remained unchanged. Independent review is the next gate, not another feature milestone.</p>'''
