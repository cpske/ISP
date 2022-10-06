---
title: User Stories
---

## What are User Stories

According to [Atlassian][atlassian-user-stories]:

> A **user story** is an informal explanation of a software feature written from the perspective of the end user. Its purpose is to articulate how a software feature will provide value to the customer.


[atlassian-user-stories]: https://www.atlassian.com/agile/project-management/user-stories
[agile-user-stories]: http://guide.agilealliance.org/guide/stories.html

## User Story Templates

```
{n}. Title of User Story

As a (stakeholder | type-of-user)
I want to (do something | achieve something)
So that (goal).

```

A less common template is:

```
As a (stakeholder | type-of-user)
In order to (objective)
I want (to do something|achieve something)
```

### Example

```
As a small business owner,
In order to improve speed that customers checkout and pay for items,
I want the POS to quickly scan barcodes and create line items for things a customer buys.
```

Acceptance Criteria:

1. POS correctly scans 95% of barcodes on products and correctly creates a sale line item for each product scanned
2. POS records incorrect product incorrectly in less than 1% of trials

Notes:

1. If the same product is scanned more than once, the POS should update the quantity of the sale line item instead of creating a new sale line item.
