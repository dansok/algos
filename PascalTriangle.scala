object PascalTriangle {
	val lookup_table = new collection.mutable.HashMap[(Int, Int), Int]
	def compute(row: Int, col: Int): Int = {
		require(col >= 0 && row >= 0, "row and col arguemnts must be >= 0")
		require(col <= row, "col must be <= row")

		if (col == 0 || col == row) {
			1
		} else {
			val r1c: Int = this.lookup_table.getOrElseUpdate((row-1, col),
				compute(row-1, col))
			val r1c1: Int = this.lookup_table.getOrElseUpdate((row-1, col-1),
				compute(row-1, col-1))
			r1c + r1c1
		}
	}
	def main(args: Array[String]): Unit = {
		val row = args(0).toInt;
		val col = args(1).toInt;
		println(this.compute(row, col))
	}
}