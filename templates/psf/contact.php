<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <title>CONTACT US</title>
</head>
<body class="bg-[#ffffff]">
    <?php
        include 'navbar.php'
    ?>
    <main>
        <div class="lg:mx-[200px] mx-[20px] my-[100px] flex flex-col justify-center">
            <div class="w-[100%]">
                <div class="w-[100%] pb-[17px] flex lg:flex-row flex-col justify-between">
                    <div class="lg:w-[50%] w-[100%]">
                        <img src="https://images.squarespace-cdn.com/content/v1/5d94a2dd7046bc4760c90517/1616334255887-OFJC7PPE9FKCDAFHOMUP/unsplash-image-xG8IQMqMITM.jpg?format=2500w" alt="">
                    </div>
                    <div class="lg:w-[50%] w-[100%] lg:text-[24px] text-[20px] lg:p-[42px] p-[34.7px] flex flex-col justify-center items-center space-y-2 text-center text-[rgba(0,0,0,.68)]">
                        <p class="text-[#bdbdbd] font-semibold font-['proxima-nova'] leading-[24px] uppercase tracking-[.3rem] mb-2">LET’S CONNECT</p>
                        <p class="font-['adobe-garamond-pro']">If you are looking at this page, you probably share our passion for security studies !</p>
                        <p class="font-['adobe-garamond-pro']">Feel free to discover and discuss our content, and if you have questions, wish to develop a partnership or to become an author, drop us a message.</p>
                    </div>
                </div>
                <div class="lg:w-[745px] w-[100%] text-[rgba(26,26,26,.7)]">
                    <div>

                    </div>
                </div>
            </div>
            <div class="pb-[17px]">
                <form action="#">
                    <div class="grid lg:grid-cols-2 lg:gap-4 grid-cols-1">
                        <div class="py-2">
                            <label for="fname" class="text-[rgba(26,26,26,.7)] text-[18px] font-['adobe-garamond-pro']">First Name <span class="text-[12px]">(required)</span></label>
                            <input type="text" class="fname border-2 border-solid border-[#a9a9a9] bg-[#fafafa] text-[#000] h-[46px] p-[10px] w-[100%]" id="fname">
                        </div>
                        <div class="py-2">
                            <label for="lname" class="text-[rgba(26,26,26,.7)] text-[18px] font-['adobe-garamond-pro']">Last Name <span class="text-[12px]">(required)</span></label>
                            <input type="text" class="lname border-2 border-solid border-[#a9a9a9] bg-[#fafafa] text-[#000] h-[46px] p-[10px] w-[100%]" id="fname">
                        </div>
                    </div>
                    <div class="py-2">
                        <label for="email" class="text-[rgba(26,26,26,.7)] text-[18px] font-['adobe-garamond-pro']">Email <span class="text-[12px]">(required)</span></label>
                        <input type="email" class="email border-2 border-solid border-[#a9a9a9] bg-[#fafafa] text-[#000] h-[46px] p-[10px] w-[100%]" id="fname">
                    </div>
                    <div class="py-2">
                        <label for="subject" class="text-[rgba(26,26,26,.7)] text-[18px] font-['adobe-garamond-pro']">Subject <span class="text-[12px]">(required)</span></label>
                        <input type="text" class="subject border-2 border-solid border-[#a9a9a9] bg-[#fafafa] text-[#000] h-[46px] p-[10px] w-[100%]" id="fname">
                    </div>
                    <div class="py-2">
                        <label for="message" class="text-[rgba(26,26,26,.7)] text-[18px] font-['adobe-garamond-pro']">Message <span class="text-[12px]">(required)</span></label>
                        <textarea name="message" id="message" rows="4" class="border-2 border-solid border-[#a9a9a9] bg-[#fafafa] text-[#000] w-[100%]"></textarea>
                    </div>
                    <div class="py-4 flex justify-center items-center">
                        <button type="submit" class="text-[#000] uppercase bg-[#FFCB05] py-[14px] px-6 hover:bg-[#000] hover:text-[#FFCB05] font-semibold">submit</button>
                    </div>
                </form>
            </div>
        </div>
    </main>
    <?php
        include 'footer.php'
    ?>
</body>
</html>