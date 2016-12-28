# HiCshapes

Human cells contain approximately three billion bases of DNA, which would measure three
meters in length if laid in a line [14]. As these cells are only on the order of 10 µm in
size, significant folding and compaction of the DNA is necessary. There are many levels of
DNA organization, ranging from unorganized open regions called euchromatin, to compact
heterocrhomatin sections wrapped around histones, all the way up to the most condensed
chromosomal form [14]. A common misconception is that DNA exists in tight x-shaped
chromosomes throughout the entirety of the cell cycle, when these bundles are actually only
formed during cell division. In most of a cell’s life its DNA is in a semi-compacted state
within the nucleus. Some regions are tightly wound and inaccessible, while others are open.
Perhaps even more surprising is the dynamic nature of DNA, where the accessibility of different
portions is constantly changing depending on the state of the cell [6].
DNA compaction serves as a mechanism to both address space limitation, and also to regulate
which genes are turned off and on. Genes within tight heterochromatin are inaccessible
to RNA polymerase and transcription factors, and cannot be turned into an active protein.
Euchromatin, on the other hand, is more actively expressed. Adding additional complexity,
certain DNA elements called enhancers can regulate transcription of genes millions of bases
away on the same or different chromosomes. In order for a cell to control which genes it is
expressing at a certain time, it must therefore carefully fold it’s entire chromosome to ensure
appropriate interactions occur. Consequently, researchers have long desired to start with
chromosome conformation data and work backwards to understand the state of a cell.
Understanding the folding interactions of chromosomes is problematic because of the shear
length of DNA and difficulty to capture these folds in physiological conditions. Some of the
first approaches to investigate DNA structure were based on microscopy and molecular probes
[13]. Examples of such methods are Fluorescent In Situ Hybridization (FISH) and Fluorescence
Resonance Energy Transfer (FRET). While these techniques are useful, they can only
be used to observe a few specific loci at a time, and cannot easily be scaled up. With the
increasing ease of sequencing, however, methods were produced to yield full chromosomal
conformation maps.

As stated above, the question of how DNA folds from invisible meter length strands to tight
observable chromosomes, has long been of interest. Chromatin conformation capture (3C) is
a relatively new technique used to describe the shape of compact DNA with massive throughput.
The original high-throughput method was published by Dekker et. al in a highly-cited
2002 paper [3]. The essence of the technique is that a population of cells are suddenly fixed
with formaldehyde or an alternate cross linker, effectively taking a snapshot of which pieces of
chromosome are neighbors [6]. Then through the clever use of restriction enzymes, the pieces
of nearby DNA are joined into a single strand that is able to be sequenced. If two sequences
not normally adjacent are read out, then a count is added to the interaction matrix between
these two regions. Note that 3C requires that the chromosome sequence is known, and the
technique cannot be used in areas of highly repetitive DNA. It is not possible to confidently
map where the interaction took place in such regions. Additional extensions to 3C, such
as 4C, 5C, HiC, and ChIA-PET have since been produced and have varying strengths and
weaknesses [5]. The applications of these tools have helped describe the biology of chromatin
conformation on incredible scales [9][12].

As with all large-data producing techniques, the analysis of 3C results is often difficult and
conclusions can vary with different approaches [7]. Furthermore, quite a bit of human inter-
1
action with the data is still necessary to find even simple patterns, such as domains, with
high confidence [4]. In this work we apply machine learning as a conducive method towards
identifying previously unstudied patterns in chromosome interaction data sets. We first use
supervised learning to show that patterns identified by a user can be learned by tensor flow
models, and then transition into unsupervised methods to delve even more deeply into the
possibilities of discovery without human intervention.
