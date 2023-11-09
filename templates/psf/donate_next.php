<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <title>Donate</title>
</head>
<body class="bg-[#ffffff]">
    <?php
        include 'navbar.php'
    ?>
    <main>
        <div class="lg:mx-[450px] mx-[20px] my-[100px]">
            <div class="flex flex-col justify-center items-center space-y-6">
                <h1 class="text-[48px] text-[#FFCB05] font-bold font-['Oswald']">Donor Info</h1>
                <h1>Please fill out the form below to complete your payment.</h1>
                <div class="w-[100%]">
                    <form action="#" class="">
                        <h1 class="text-[48px] text-center text-black font-bold font-['Oswald']">Your Details</h1>
                        <div class="py-2">
                            <label for="name" class="text-[#000] text-[18px] font-['adobe-garamond-pro']">Your Name <span class="text-[12px]">(required)</span></label>
                            <input type="text" class="name bg-[#fffae6] text-[#000] h-[46px] p-[10px] w-[100%]" id="name" placeholder="Enter Your Name">
                        </div>
                        <div class="py-2">
                            <label for="email" class="text-[#000] text-[18px] font-['adobe-garamond-pro']">Your Email <span class="text-[12px]">(required)</span></label>
                            <input type="text" class="email bg-[#fafafa] text-[#000] h-[46px] p-[10px] w-[100%]" id="email" placeholder="Enter Your Email">
                        </div>
                        <div class="py-2">
                            <label for="phone" class="text-[#000] text-[18px] font-['adobe-garamond-pro']">Your Phone Number <span class="text-[12px]">(required)</span></label>
                            <input type="text" class="phone bg-[#fafafa] text-[#000] h-[46px] p-[10px] w-[100%]" id="phone" placeholder="Enter Your Phone Number">
                        </div>
                        <div>
                            <button type="submit" id="submit" class="w-[100%] py-[8px] px-[30px] text-center cursor-pointer text-[18px] bg-[#FFCB05] text-black hover:text-[#FFCB05] hover:bg-[#2b2b2b]">Proceed to Payment »</button>
                        </div>
                    </form>
                </div>
                <div>
                    <img src="https://i.postimg.cc/fLFV9qvg/ssl.png" alt="">
                </div>
            </div>
        </div>
    </main>
    <?php
        include 'footer.php'
    ?>
</body>
</html>