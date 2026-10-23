-- Read-only rural showcase inspection. Never shipped in the playable package.
local function report(label, actual, expected)
    print("[Rural QA] " .. (actual == expected and "PASS" or "FAIL") .. " " .. label
        .. " actual=" .. tostring(actual) .. " expected=" .. tostring(expected))
end

local function runChecks()
    local player, cell = getSpecificPlayer(0), getCell()
    if not player or not cell then return end
    local function square(x, y) return cell:getGridSquare(120 + x, 120 + y, 0) end
    local function hasSprite(x, y, name)
        local s = square(x, y)
        if not s then return false end
        for i = 0, s:getObjects():size() - 1 do
            local sprite = s:getObjects():get(i):getSprite()
            if sprite and sprite:getName() == name then return true end
        end
        return false
    end
    local deck = 0
    for y = 1, 8 do
        for x = -4, -1 do
            if hasSprite(x, y, "carpentry_02_56") then deck = deck + 1 end
        end
    end
    report("deck squares", deck, 32)
    report("planting touching south facade", hasSprite(0, 10, "vegetation_ornamental_01_16")
        or hasSprite(0, 10, "vegetation_ornamental_01_17")
        or hasSprite(0, 10, "vegetation_ornamental_01_18"), true)
    report("planting touching east facade", hasSprite(6, 3, "vegetation_ornamental_01_16")
        or hasSprite(6, 3, "vegetation_ornamental_01_17")
        or hasSprite(6, 3, "vegetation_ornamental_01_18"), true)
    report("barbecue", hasSprite(-4, 7, "appliances_cooking_01_35"), true)
    report("wheelie bin", hasSprite(10, 13, "trashcontainers_01_0"), true)
    report("wood stack", hasSprite(10, 14, "camping_01_26")
        and hasSprite(10, 15, "camping_01_27"), true)
    report("garden bird bath", hasSprite(4, 19, "vegetation_ornamental_01_50"), true)
    report("front boundary", hasSprite(-5, -3, "fencing_01_4"), true)
    local blocked = 0
    for y = 3, 4 do
        for x = -6, -2 do
            local s = square(x, y)
            if not s or s:testCollideAdjacent(player, 1, 0, 0) then blocked = blocked + 1 end
        end
    end
    report("blocked front approach edges", blocked, 0)
    local s = square(-5, -3)
    report("picket boundary collision", s and s:testCollideAdjacent(player, -1, 0, 0), true)
    local landings = 0
    for _, xy in ipairs({{-1,1},{-1,7},{2,-1},{6,2},{6,7},{2,10},{5,10}}) do
        local landing = square(xy[1], xy[2])
        if landing and landing:isFree(false) then landings = landings + 1 end
    end
    report("free window landings", landings, 7)
    local framed = 0
    for _, xy in ipairs({{0,1},{0,7},{2,0},{6,2},{6,7},{2,10},{5,10}}) do
        local found = false
        for _, name in ipairs({"walls_exterior_house_07_120", "walls_exterior_house_07_121",
                               "walls_interior_house_07_24", "walls_interior_house_07_25"}) do
            if hasSprite(xy[1], xy[2], name) then found = true end
        end
        if found then framed = framed + 1 end
    end
    report("windows with surrounding wall", framed, 7)
end
Events.OnGameStart.Add(runChecks)
