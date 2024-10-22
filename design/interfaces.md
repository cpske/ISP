
## Interface in Python?

Python does not really have interfaces, but it has **two** mechanisms that behave like interfaces.

1. Abstract Base Classes with abstract methods.

2. The `zope.interface` in the `zope` package.
   - ```pip install zope```
   ```python
   from zope.interface import Interface

   class Polygon(Interface):
       """An interface for behavior of polygons."""

       def perimeter(self):
           """Return the perimeter of the polygon."""

       def area(self):
           """Return the area of the polygon."""
    ```
    - classes that implement the interface should add an `implementer` decorator:
    ```python
    from zope.interface import implementer
    @implementer(Polygon)
    class Rectange:
    ```

3. ???

