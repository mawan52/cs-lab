#import "@local/knowledge:1.0.0": *
#import "@preview/cetz:0.5.2"

#let todo = {
  block(
    inset: 10pt,
    fill: orange.lighten(80%),
    stroke: 3pt + orange,
    width: 100%,
    align(
      center,
      text(
        fill: orange,
        weight: 650,
        "TODO",
      ),
    ),
  )
}

#show: knowledge.with(
  authors: ("mawan",),
  title: [CS Lab],
  subtitle: [Laboratories],
  // front-image: image("./_img/_cover.jpg"),
  date: [2026],
)

#include "chapters/algorithms.typ"
