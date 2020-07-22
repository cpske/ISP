

 After doing the Django tutorial, explain how
  relationships are mapped to database tables.
   - identity field as key.  Synthetic id, sequence, natural id, or compound key
   - many-to-1, 1-to-1 (not that common), 1-to-many
   - Foreign Keys 
   - cascading (cascading save, cascading delete) for foreign-key objects
   - lazy instantiation
   - object uniqueness for entities
   - 2 design patterns: DAO and Active Object
   - anti-pattern: anemic models (and fat controllers)