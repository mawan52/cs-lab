#import "@local/knowledge:1.0.0": *

#show: knowledge.with(
  authors: ("mawan",),
  title: [CS Lab],
  subtitle: [Laboratories],
  // front-image: image("./_img/_cover.jpg"),
  date: [2026],
)

// #set text(
//   font: "Open Sans"
// )

= Algorithms
First of all, what is an algorithm?

The word itself has an origin story that traces
back to Persian scientist and polymath
#link("https://en.wikipedia.org/wiki/Al-Khwarizmi")[Al-Khwarizmi].
Al-Khwarizmi's work on arithmetic introduced systematic calculation
methods and the Arabic numeral system to medieval Europe. He also
presented clear, step-by-step procedures for solving common
arithmetic and algebraic problems.
The world "algorithm" is derived from the latinised form of his name.

An algorithm itself is a sequence of well-defined instructions
used to perform a particular task. Furthermore, an algorithm may
receive an input, process it, and deliver an output.
A complete algorithm must terminate after a finite number of steps.

Having covered the words origin and meaning, the rest of this chapter aims
to introduce some of the most important algorithms in computer science.

== Sorting
One of the most frequently recurring tasks in day-to-day lives is the
sorting of elements. Regardless of what is being sorted,
there is always a systematic approach behind the sorting process.

For example, when sorting a list of numbers ascendingly, one
could repeatedly find the smallest number in the unsorted part of the
list and swap it with the first number in that part.
This approach is known as
#link("https://en.wikipedia.org/wiki/Selection_sort")[selection sort]
or more specifically, min sort.

=== The problem
Imagine you are handed a large pile of documents that have to be arranged
according to their page numbers. While sorting a small number of papers by
hand sounds feasible, the process becomes increasingly time-consuming and
error-prone as the number of pages increases.
Therefore, a systematic sorting method is needed. Two commonly used methods
for solving this type of problem are Merge Sort (@merge-sort) and Quick Sort
(@quick-sort).

=== Merge Sort <merge-sort>
Merge Sort utilises the "divide-and-conquer" principle to solve the
problem presented above. First, the given list has to be recursively
split into two halves. When every list is made up of exactly 1 element,
they can be merged and sorted back together.

 It works by recursively splitting the given
list into two halves, and then merging them back toghether

=== Quick Sort <quick-sort>
