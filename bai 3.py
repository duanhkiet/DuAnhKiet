from ._anvil_designer import Form1Template
from anvil import 

class Form1(Form1Template)
  def __init__(self, properties)
        # Set up theme support
        self.init_components(properties)

        # Thêm các thuộc tính cho Dropdown
        self.drop_down_1.items = [Insertion Sort, Selection Sort, Bubble Sort, Merge Sort]

  def button_1_click(self, event_args)
        # Nhận dãy số từ TextBox và chuyển đổi sang danh sách các số nguyên
        numbers_str = self.text_box_1.text.split( )
        numbers = []
        for num in numbers_str
            num = num.strip()  # Loại bỏ các khoảng trắng ở đầu và cuối chuỗi
            if num
                numbers.append(int(num))  # Chỉ chuyển đổi thành số nguyên nếu chuỗi không rỗng

        # Chọn thuật toán sắp xếp từ DropDown
        algorithm = self.drop_down_1.selected_value

        # Sắp xếp dãy số bằng thuật toán được chọn
        sorted_numbers = self.sort_numbers(numbers, algorithm)

        # Hiển thị kết quả sắp xếp trên Label
        self.label_3.text = Dãy số sau khi sắp xếp  + , .join(map(str, sorted_numbers))

  def sort_numbers(self, numbers, algorithm)
        # Sắp xếp dãy số bằng thuật toán được chọn
        if algorithm == Insertion Sort
            self.insertion_sort(numbers)
        elif algorithm == Selection Sort
            self.selection_sort(numbers)
        elif algorithm == Bubble Sort
            self.bubble_sort(numbers)
        elif algorithm == Merge Sort
            self.merge_sort(numbers)
        return numbers

    # Thuật toán sắp xếp Insertion Sort
  def insertion_sort(self, arr)
        for i in range(1, len(arr))
            key = arr[i]
            j = i - 1
            while j = 0 and arr[j]  key
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    # Thuật toán sắp xếp Selection Sort
  def selection_sort(self, arr)
        for i in range(len(arr))
            min_idx = i
            for j in range(i + 1, len(arr))
                if arr[j]  arr[min_idx]
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    # Thuật toán sắp xếp Bubble Sort
  def bubble_sort(self, arr)
        n = len(arr)
        for i in range(n)
            for j in range(0, n - i - 1)
                if arr[j]  arr[j + 1]
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # Hàm merge cho Merge Sort
  def merge(self, arr, l, m, r)
        n1 = m - l + 1
        n2 = r - m

        L = arr[lm + 1]
        R = arr[m + 1r + 1]

        i = j = 0
        k = l

        while i  n1 and j  n2
            if L[i] = R[j]
                arr[k] = L[i]
                i += 1
            else
                arr[k] = R[j]
                j += 1
            k += 1

        while i  n1
            arr[k] = L[i]
            i += 1
            k += 1

        while j  n2
            arr[k] = R[j]
            j += 1
            k += 1

    # Thuật toán sắp xếp Merge Sort
  def merge_sort(self, arr)
        if len(arr)  1
            mid = len(arr)  2
            L = arr[mid]
            R = arr[mid]

            self.merge_sort(L)
            self.merge_sort(R)

            self.merge(arr, 0, mid - 1, len(arr) - 1)
